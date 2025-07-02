from playwright.sync_api import sync_playwright


def main():
    NUMBER = 18024
    fh = open("equity.txt", "w", encoding="utf-8")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        c = 0
        k = 0
        while c < NUMBER:
            # URL = f"https://ca.finance.yahoo.com/research-hub/screener/etf/?start={c}&count=100"
            URL = f"https://ca.finance.yahoo.com/research-hub/screener/equity/?start={c}&count=100"
            page.goto(URL)
            c += 100
            for i in range(1, 101):
                symbol = f'//*[@id="nimbus-app"]/section/section/section/article/section/div/div[5]/div[1]/table/tbody/tr[{i}]/td[2]/div/span/a/div'
                cell = page.locator(symbol)
                value = cell.text_content().strip()  # type: ignore
                fh.write(f"{value}\n")
                print(value)
                k += 1
                if k > NUMBER - 1:
                    break
        browser.close()
        fh.close()


if __name__ == "__main__":
    main()
