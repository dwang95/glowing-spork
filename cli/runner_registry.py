
from foundations.runner import Runner
from lottery.branch.runner import BranchRunner
from lottery.runner import LotteryRunner
from training.runner import TrainingRunner

registered_runners = {'train': TrainingRunner, 'lottery': LotteryRunner, 'lottery_branch': BranchRunner}


def get(runner_name: str) -> Runner:
    if runner_name not in registered_runners:
        raise ValueError('No such runner: {}'.format(runner_name))
    else:
        return registered_runners[runner_name]
