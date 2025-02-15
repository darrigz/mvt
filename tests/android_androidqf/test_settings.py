# Mobile Verification Toolkit (MVT)
# Copyright (c) 2021-2023 Claudio Guarnieri.
# Use of this software is governed by the MVT License 1.1 that can be found at
#   https://license.mvt.re/1.1/

from pathlib import Path

from mvt.android.modules.androidqf.settings import Settings
from mvt.common.module import run_module

from ..utils import get_android_androidqf, list_files


class TestSettingsModule:
    def test_parsing(self):
        data_path = get_android_androidqf()
        m = Settings(target_path=data_path)
        files = list_files(data_path)
        parent_path = Path(data_path).absolute().parent.as_posix()
        m.from_folder(parent_path, files)
        run_module(m)
        assert len(m.results) == 1
        assert "random" in m.results.keys()
        assert len(m.detected) == 0
