#!/usr/bin/env python3
import argparse
import time
import typing
from playwright.sync_api import Playwright, sync_playwright, expect


class LoginInfo(typing.NamedTuple):
    username: str
    password: str


# Whenever you create an account for a student is scratch, it asks them to fill
# out a questionaire. This can be quite disruptive in the middle of class, so
# this script automatically goes through and fills the questionaire with data
# so the students can "get right to it".


def fill_in_form(playwright: Playwright, name: str, password: str) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://scratch.mit.edu/")
    page.get_by_role("link", name="Sign in").click()
    page.locator("#frc-username-1088").click()
    time.sleep(1)
    page.locator("#frc-username-1088").fill(name)
    page.locator("#frc-password-1088").click()
    page.locator("#frc-password-1088").fill(password)
    time.sleep(1)  # This is needed otherwise "Sign in" doesn't think stuff is populated
    page.get_by_role("button", name="Sign in").click()
    time.sleep(1)
    page.get_by_role("button", name="Get Started").click()
    time.sleep(1)
    page.get_by_label("Birth Year *").select_option("2014")
    page.get_by_label("", exact=True).first.check()
    page.locator("[id=\"frc-user\\.genderOther-1088\"]").click()
    page.locator("[id=\"frc-user\\.genderOther-1088\"]").fill("N/A")
    page.get_by_label("Country *").select_option("United States of America")
    time.sleep(2)
    page.get_by_role("button", name="Next Step").click()
    time.sleep(2)
    page.get_by_role("button", name="Go to Class").click()
    time.sleep(2)

    # ---------------------
    context.close()
    browser.close()



def scratch_initial_info_filler(csv_path: str) -> None:

    login_infos = []
    with open(csv_path, "r") as csv_fp:
        for line in csv_fp:
            line = line.strip()
            s = line.split(",")
            assert len(s) == 2
            login_infos.append(LoginInfo(username=s[0], password=s[1]))

    with sync_playwright() as playwright:
        for count, login_info in enumerate(login_infos):
            print(count, login_info)
            fill_in_form(playwright, login_info.username, login_info.password)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Path to .csv file", type=str, required=True)
    args = parser.parse_args()

    scratch_initial_info_filler(args.path)
