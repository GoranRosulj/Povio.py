from playwright.sync_api import Page, Locator

class SignUpPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.sign_up_header = page.locator('h3:has-text("Sign up")')
        self.user_name = page.locator('#user_name')
        self.user_email = page.locator('#user_email')
        self.user_password = page.locator('#user_password')
        self.user_password_confirm = page.locator('#user_password_confirmation')
        self.sign_up_button = page.locator('.button')
        self.error_explanation = page.locator('#error_explanation > ul > li')

    async def get_sign_up_text(self) -> str:
        return await self.sign_up_header.text_content()

    async def fill_user_name_field(self, user_name: str):
        await self.user_name.fill(user_name)

    async def fill_user_email_field(self, user_email: str):
        await self.user_email.fill(user_email)

    async def fill_user_pass_field(self, user_pass: str):
        await self.user_password.fill(user_pass)

    async def fill_user_pass_confirm_field(self, user_pass_confirm: str):
        await self.user_password_confirm.fill(user_pass_confirm)

    async def click_on_sign_up(self):
        await self.sign_up_button.click()

    async def get_error_message(self) -> str:
        return await self.error_explanation.text_content()

    async def register_new_user(self, user_name: str, user_email: str, user_password: str):
        await self.fill_user_name_field(user_name)
        await self.fill_user_email_field(user_email)
        await self.fill_user_pass_field(user_password)
        await self.fill_user_pass_confirm_field(user_password)
        await self.click_on_sign_up()
