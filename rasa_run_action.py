#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022-08-26 17:23
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    rasa_run_action.py
# @Project: rasa-3.x-action-examples
# @Package:
# @Ref:


from rasa_sdk.endpoint import run

run(
    action_package_name="actions",
    port=5055
)
