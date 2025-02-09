from playwright.sync_api import Page, Locator

class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.welcome = page.locator('h3:has-text("Welcome")')

    async def navigate(self):
        await self.page.goto(BASE_URL)  # Ensure BASE_URL is set in your environment variables

    # A method to get the welcome text
    async def get_welcome_text(self) -> str:
        return await self.welcome.text_content()

    async def click_on_link(self, link_name: str):
        # Use the locator to find the link by its text and click it
        await self.page.locator(f'a:has-text("{link_name}")').click()
