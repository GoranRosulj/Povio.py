from playwright.test import page, expect

class CommonUIComponents:
    def __init__(self, page):
        self.page = page
        self.logo = page.locator("a.logo")
        self.homePageLinks = lambda link_name: page.locator(f'a:has-text("{link_name}")')
        self.flashNotice = page.locator("#flash_notice")
        self.flashAlert = page.locator("#flash_alert")
        self.flashXButton = page.locator(".close")

    # A method to click on a link by text
    async def click_link(self, link_name):
        await self.homePageLinks(link_name).click()

    # A method to get a link text
    async def get_link_text(self, link_name):
        return await self.homePageLinks(link_name).text_content()

    # A method to get the flash notice text
    async def get_flash_notice_text(self):
        return await self.flashNotice.text_content()
    
    # A method to get the flash alert text
    async def get_flash_alert_text(self):
        return await self.flashAlert.text_content()
    
    # A method to verify the flash notice is visible
    async def verify_flash_notice(self):
        await expect(self.flashNotice).to_be_visible()
    
    # A method to verify the flash alert is visible
    async def verify_flash_alert(self):
        await expect(self.flashAlert).to_be_visible()
    
    # A method to verify the flash x button is visible
    async def verify_flash_x_button(self):
        await expect(self.flashXButton).to_be_visible()
    
    # A method to verify the logo is visible
    async def verify_logo(self):
        await expect(self.logo).to_be_visible()
    
    # A method to click the flash x button
    async def click_flash_x_button(self):
        await self.flashXButton.click()
