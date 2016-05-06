#!/bin/bash

branch="master"

  git fetch origin
  # Check which files have changed
  DIFFLIST=$(git --no-pager diff --name-only "$branch..origin/$branch")
  git pull
  git fetch origin
  git checkout "$branch"
  git reset --hard "origin/$branch" && git clean -f -d
  # Set permissions
  chmod -R 744 ./*
