#!/usr/bin/env python3
# encoding: utf-8
from __future__ import annotations

import argparse
import os
import sys

import __version__

# setup access to the local .site-packages
sys.path.insert(
    0, os.path.dirname(os.path.abspath(__file__)) + "/.site-packages"
)  # noqa

import workflow
from workflow import Workflow3
import CoreFoundation
from CoreServices import LaunchServices


def get_current_default_browser():
    return LaunchServices.LSCopyDefaultRoleHandlerForContentType(
        CoreFoundation.CFSTR("public.html"), LaunchServices.kLSRolesViewer
    )


def get_browsers():
    return LaunchServices.LSCopyAllRoleHandlersForContentType(
        CoreFoundation.CFSTR("public.html"), LaunchServices.kLSRolesViewer
    )


def set_browser(browser: str):
    LaunchServices.LSSetDefaultHandlerForURLScheme(
        CoreFoundation.CFSTR("http"), CoreFoundation.CFSTR(browser)
    )


def main(wf: Workflow3):
    try:
        current_default = get_current_default_browser()
        browsers = get_browsers()
        for browser in browsers:
            if browser == current_default:
                wf.add_item(title=browser, icon=workflow.ICON_FAVOURITE, valid=False)
            else:
                wf.add_item(
                    title=browser, icon=workflow.ICON_WEB, valid=True, arg=browser
                )

        wf.send_feedback()
    except Exception as e:
        wf.logger.exception(e)
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s", "--set", help="the requested new default browser")
    group.add_argument(
        "-c", "--current", help="prints current default browser", action="store_true"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"{parser.prog} {__version__.__version__}",
    )
    args = parser.parse_args()

    if args.set:
        set_browser(args.set)
    elif args.current:
        print(get_current_default_browser())
    else:
        # Create a global `Workflow3` object
        nwf = Workflow3()
        # Call your entry function via `Workflow3.run()` to enable its
        # helper functions, like exception catching, ARGV normalization,
        # magic arguments etc.
        nwf.run(main)
