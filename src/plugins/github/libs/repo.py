#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2021-03-12 15:36:14
@LastEditors    : yanyongyu
@LastEditTime   : 2021-06-15 22:16:20
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

from typing import Optional

from src.libs.github import Github
from src.libs.github.models import Repository

from .. import github_config as config


async def get_repo(
    owner: str, repo_name: str, token: Optional[str] = None
) -> Repository:
    if token:
        g = Github(token)
    elif config.github_client_id and config.github_client_secret:
        g = Github(config.github_client_id, config.github_client_secret)
    else:
        g = Github()

    async with g:
        return await g.get_repo(f"{owner}/{repo_name}", False)
