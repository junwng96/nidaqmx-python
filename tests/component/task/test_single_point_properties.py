import pytest

from nidaqmx.constants import WaitMode
from nidaqmx.task import Task


@pytest.fixture()
def ai_voltage_task(task, sim_4311_device):
    """Gets AI voltage task."""
    task.ai_channels.add_ai_voltage_chan(sim_4311_device.ai_physical_chans[0].name)
    yield task


def test___ai_task___get_conv_late_errors_to_warnings___returns_default_value(
    ai_voltage_task: Task,
):
    assert ai_voltage_task.single_point.conv_late_errors_to_warnings == False


def test___ai_task___set_conv_late_errors_to_warnings___returns_assigned_value(
    ai_voltage_task: Task,
):
    ai_voltage_task.single_point.conv_late_errors_to_warnings = True

    assert ai_voltage_task.single_point.conv_late_errors_to_warnings == True


def test___ai_task___reset_conv_late_errors_to_warnings___returns_default_value(
    ai_voltage_task: Task,
):
    ai_voltage_task.single_point.conv_late_errors_to_warnings == True

    del ai_voltage_task.single_point.conv_late_errors_to_warnings

    assert ai_voltage_task.single_point.conv_late_errors_to_warnings == False


def test___ai_task___get_num_of_warmup_iters_property___returns_default_value(
    ai_voltage_task: Task,
):
    assert ai_voltage_task.single_point.num_of_warmup_iters == 0


def test___ai_task___get_report_missed_samples_property___returns_default_value(
    ai_voltage_task: Task,
):
    assert ai_voltage_task.single_point.report_missed_samples == False


def test___ai_task___get_wait_for_next_samp_clk_wait_mode___returns_default_value(
    ai_voltage_task: Task,
):
    assert (
        ai_voltage_task.single_point.wait_for_next_samp_clk_wait_mode == WaitMode.WAIT_FOR_INTERRUPT
    )


def test___ai_task___set_wait_for_next_samp_clk_wait_mode___returns_assigned_value(
    ai_voltage_task: Task,
):
    ai_voltage_task.single_point.wait_for_next_samp_clk_wait_mode = WaitMode.SLEEP

    assert ai_voltage_task.single_point.wait_for_next_samp_clk_wait_mode == WaitMode.SLEEP


def test___ai_task___reset_wait_for_next_samp_clk_wait_mode___returns_default_value(
    ai_voltage_task: Task,
):
    ai_voltage_task.single_point.wait_for_next_samp_clk_wait_mode == WaitMode.SLEEP

    del ai_voltage_task.single_point.wait_for_next_samp_clk_wait_mode

    assert (
        ai_voltage_task.single_point.wait_for_next_samp_clk_wait_mode == WaitMode.WAIT_FOR_INTERRUPT
    )
