"""Tests for fmripost_rapidtide.workflows."""

from fmripost_rapidtide import config
from fmriprep.workflows.tests import mock_config


def test_init_rapidtide_wf(tmp_path_factory):
    from fmripost_rapidtide.workflows.rapidtide import init_rapidtide_wf

    tempdir = tmp_path_factory.mktemp('test_init_rapidtide_wf')

    with mock_config():
        config.execution.output_dir = tempdir / 'out'
        config.execution.work_dir = tempdir / 'work'
        config.workflow.denoise_method = ['nonaggr', 'orthaggr']
        config.workflow.melodic_dim = -200
        config.workflow.err_on_warn = False

        wf = init_rapidtide_wf(
            bold_file='sub-01_task-rest_bold.nii.gz',
            metadata={'RepetitionTime': 2.0},
        )
        assert wf.name == 'rapidtide_task_rest_wf'


def test_init_denoise_wf(tmp_path_factory):
    from fmripost_rapidtide.workflows.rapidtide import init_denoise_wf

    tempdir = tmp_path_factory.mktemp('test_init_denoise_wf')

    with mock_config():
        config.execution.output_dir = tempdir / 'out'
        config.execution.work_dir = tempdir / 'work'

        wf = init_denoise_wf(bold_file='sub-01_task-rest_bold.nii.gz')
        assert wf.name == 'denoise_task_rest_wf'