#!/usr/bin/env python3
# encoding: utf-8
from __future__ import annotations

import argparse
import os
import sys

import __version__

# setup access to the local lib directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/lib")  # noqa

from workflow import Workflow
import objc
import CoreFoundation
from CoreServices import LaunchServices


def get_current_default_browser():
    # In theory LSCopyDefaultRoleHandlerForContentType is deprecated
    # https://developer.apple.com/documentation/coreservices/1449868-lscopydefaultrolehandlerforconte?language=objc
    return LaunchServices.LSCopyDefaultRoleHandlerForContentType(
        CoreFoundation.CFSTR("public.html"), LaunchServices.kLSRolesViewer
    )


def get_browsers():
    # In theory LSCopyAllRoleHandlersForContentType is deprecated
    # https://developer.apple.com/documentation/coreservices/1448020-lscopyallrolehandlersforcontentt?language=objc
    return LaunchServices.LSCopyAllRoleHandlersForContentType(
        CoreFoundation.CFSTR("public.html"), LaunchServices.kLSRolesViewer
    )


def get_browser_url(bundle_id):
    # https://developer.apple.com/documentation/coreservices/1449290-lscopyapplicationurlsforbundleid?language=objc
    apps = LaunchServices.LSCopyApplicationURLsForBundleIdentifier(bundle_id, objc.NULL)
    return apps[0][0]


def get_browser_display_name(url):
    name = url.lastPathComponent()
    return name


def set_browser(browser: str):
    # In theory LSSetDefaultHandlerForURLScheme is deprecated
    # https://developer.apple.com/documentation/coreservices/1447760-lssetdefaulthandlerforurlscheme?language=objc
    LaunchServices.LSSetDefaultHandlerForURLScheme(
        CoreFoundation.CFSTR("http"), CoreFoundation.CFSTR(browser)
    )


def main(wf: Workflow):
    try:
        current_default = get_current_default_browser()
        browsers = get_browsers()
        for browser in browsers:
            url = get_browser_url(browser)
            title = get_browser_display_name(url)
            path = url.path()

            if browser == current_default:
                # Use a different uid when it is currently the default. This improves suggestions.
                uid = f"current+{browser}"
                subtitle = "Current default browser"
                valid = False
                arg = None
            else:
                uid = browser
                subtitle = f"Set {title} as default browser"
                valid = True
                arg = browser

            wf.add_item(
                uid=uid,
                title=title,
                subtitle=subtitle,
                icon=path,
                icontype="fileicon",
                valid=valid,
                arg=arg,
                autocomplete=title,
                copytext=path,
                largetext=title,
                quicklookurl=url.path(),
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
        nwf = Workflow()
        nwf.run(main)
