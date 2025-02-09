from playwright.sync_api import Page, Locator

class EditAccountPage:
    
    def __init__(self, page: Page):
        self.page = page
        # Locator for the header (assuming "Edit User" is displayed).
        self.edit_page_header = page.locator('h3:has-text("Edit User")')
        # User information fields.
        self.user_name = page.locator('#user_name')
        self.user_email = page.locator('#user_email')
        self.user_password = page.locator('#user_password')
        self.user_password_confirm = page.locator('#user_password_confirmation')
        self.user_current_password = page.locator('#user_current_password')
        # Locator for the update button – from the form input with value "Update".
        self.update_button = page.locator('input.button.right[value="Update"]')
        # Locator for the error explanation.
        self.error_explanation = page.locator('#error_explanation')
        # Locator for the cancel account button, found in the cancellation form.
        self.cancel_account_button = page.locator('form.button_to input[value="Cancel my account"]')

    async def get_edit_page_header_text(self) -> str:
        return await self.edit_page_header.text_content()

    async def fill_user_name_field(self, user_name: str):
        await self.user_name.fill(user_name)

    async def fill_user_email_field(self, user_email: str):
        await self.user_email.fill(user_email)

    async def fill_user_pass_field(self, user_pass: str):
        await self.user_password.fill(user_pass)

    async def fill_user_pass_confirm_field(self, user_pass_confirm: str):
        await self.user_password_confirm.fill(user_pass_confirm)

    async def fill_user_current_password(self, user_current_pass: str):
        await self.user_current_password.fill(user_current_pass)

    async def click_on_update(self):
        await self.update_button.click()

    async def get_error_message(self) -> str:
        return await self.error_explanation.text_content()

    async def click_on_cancel_account(self):
        await self.cancel_account_button.click()
    
    # A method to change user's name
    async def update_name(self, new_name: str, current_password: str):
        await self.fill_user_name_field(new_name)
        await self.fill_user_current_password(current_password)
        await self.click_on_update()
    
    # A method to change user's email
    async def update_email(self, new_email: str, current_password: str):
        await self.fill_user_email_field(new_email)
        await self.fill_user_current_password(current_password)
        await self.click_on_update()
    
    # A method to change user's name and email
    async def update_name_and_email(self, new_name: str, new_email: str, current_password: str):
        await self.fill_user_name_field(new_name)
        await self.fill_user_email_field(new_email)
        await self.fill_user_current_password(current_password)
        await self.click_on_update()
    
    # A method to change the password
    async def update_password(self, new_password: str, current_password: str):
        await self.fill_user_pass_field(new_password)
        await self.fill_user_pass_confirm_field(new_password)
        await self.fill_user_current_password(current_password)
        await self.click_on_update()
