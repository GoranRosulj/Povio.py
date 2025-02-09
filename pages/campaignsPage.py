from playwright.sync_api import Page, Locator

class CampaignsPage:

    def __init__(self, page: Page):
        self.page = page
        # Locators for elements on the Campaigns page.
        self.campaigns_page_header = page.locator('h3:has-text("Campaigns")')
        self.add_new_campaign_link = page.locator('a:has-text("Add New Campaign")')
        self.campaign_name_field = page.locator('input[name="campaign[name]"]')
        self.campaign_description_field = page.locator('input[name="campaign[description]"]')
        self.one_time_radio = page.locator('input[type="radio"][value="one_time"]')
        self.repeatable_radio = page.locator('input[type="radio"][value="repeatable"]')
        self.create_campaign_button = page.locator('input[type="submit"][value="Create Campaign"]')
        self.update_campaign_button = page.locator('input[type="submit"][value="Update Campaign"]')
        self.campaign_table = page.locator('table.table')
        self.campaign_rows = page.locator('table.table tbody tr')
        self.campaign_edit_link = lambda name: page.locator(f'table.table tbody tr:has-text("{name}") a:has-text("Edit")')
        self.campaign_delete_link = lambda name: page.locator(f'table.table tbody tr:has-text("{name}") a[data-method="delete"]')

    async def get_campaigns_page_header_text(self) -> str:
        return await self.campaigns_page_header.text_content()

    async def navigate_to_new_campaign(self):
        await self.add_new_campaign_link.click()

    async def create_campaign(self, name: str, description: str, campaign_type: str):
        await self.campaign_name_field.fill(name)
        await self.campaign_description_field.fill(description)
        if campaign_type == 'one_time':
            await self.one_time_radio.check()
        else:
            await self.repeatable_radio.check()
        await self.create_campaign_button.click()

    async def edit_campaign(self, old_name: str, new_name: str, new_description: str):
        await self.campaign_edit_link(old_name).click()
        await self.campaign_name_field.fill(new_name)
        await self.campaign_description_field.fill(new_description)
        await self.update_campaign_button.click()

    async def delete_campaign(self, name: str):
        await self.campaign_delete_link(name).click()

    async def campaign_exists(self, campaign_name: str) -> bool:
        count = await self.campaign_rows.filter({'has_text': campaign_name}).count()
        return count > 0
