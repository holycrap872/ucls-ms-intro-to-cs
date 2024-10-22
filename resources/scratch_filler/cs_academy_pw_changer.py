#!/usr/bin/env python3
import argparse
import time
import typing
from playwright.sync_api import Playwright, sync_playwright, expect

"""
Installing playwright:
1. pip3 install playwright
2. python3 -m playwright install
"""


class LoginInfo(typing.NamedTuple):
    username: str
    old_password: str
    new_password: str


# Whenever you create an account for a student is scratch, it asks them to fill
# out a questionaire. This can be quite disruptive in the middle of class, so
# this script automatically goes through and fills the questionaire with data
# so the students can "get right to it".


def fill_in_form(playwright: Playwright, name: str, old_password: str, new_password: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://academy.cs.cmu.edu/")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Username").fill(name)
    page.get_by_placeholder("Username").press("Tab")
    page.get_by_placeholder("Password").fill(old_password)
    page.get_by_role("button", name="Log in").click()
    time.sleep(1)
    page.locator("button").filter(has_text="Agree").get_by_role("button").click()
    time.sleep(1)
    page.get_by_role("button", name="your avatar").click()
    page.get_by_role("menuitem", name="Change Password").click()
    page.get_by_label("Old Password").click()
    page.get_by_label("Old Password").fill(old_password)
    page.get_by_label("New Password", exact=True).click()
    page.get_by_label("New Password", exact=True).fill(new_password)
    page.get_by_label("Confirm New Password").click()
    page.get_by_label("Confirm New Password").fill(new_password)
    page.get_by_role("button", name="Update").click()

    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()


def cs_academy_pw_changer(csv_path: str) -> None:
    login_infos = []
    with open(csv_path, "r") as csv_fp:
        for line in csv_fp:
            line = line.strip()
            if len(line) == 0:
                # Weird 0x0D character in certain .csv dumps
                continue

            s = line.split(",")
            assert len(s) == 3
            login_infos.append(LoginInfo(username=s[0], old_password=s[1], new_password=s[2]))

    with sync_playwright() as playwright:
        for count, login_info in enumerate(login_infos):
            print(count, login_info)
            fill_in_form(playwright, login_info.username, login_info.old_password, login_info.new_password)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Path to .csv file", type=str, required=True)
    args = parser.parse_args()

    cs_academy_pw_changer(args.path)
