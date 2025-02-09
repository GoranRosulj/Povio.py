from playwright.sync_api import Page, Locator

class SignInPage:

    def __init__(self, page: Page):
        self.page = page
        self.sign_in_header = page.locator('h3:has-text("Sign in")')
        self.user_email = page.locator('#user_email')
        self.user_password = page.locator('#user_password')
        self.sign_in_button = page.locator('.button')
        self.remember_me = page.locator('#user_remember_me')
        self.error_explanation = page.locator('#error_explanation')

    # A method to fill the user email field
    async def fill_user_email_field(self, user_email: str):
        await self.user_email.fill(user_email)

    # A method to fill the user password field
    async def fill_user_pass_field(self, user_pass: str):
        await self.user_password.fill(user_pass)

    # A method to toggle the remember me checkbox
    async def toggle_remember_me(self):
        await self.remember_me.click()

    # A method to click on the sign in button
    async def click_sign_in_button(self):
        await self.sign_in_button.click()

    # A method to get the error message
    async def get_error_message(self) -> str:
        return await self.error_explanation.text_content()

    # A method to login with the given email and password
    async def login_user(self, email: str, password: str):
        await self.fill_user_email_field(email)
        await self.fill_user_pass_field(password)
        await self.click_sign_in_button()
