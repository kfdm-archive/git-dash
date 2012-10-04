import subprocess
import logging

logger = logging.getLogger(__name__)


class Git(object):
    def __init__(self, path):
        self.path = path

    def run(self, *args):
        command = ['git'] + list(args)
        return subprocess.check_output(
            command,
            cwd=self.path,
            )

    def log(self):
        commits = []
        try:
            log = self.run('log', '-n', '10', '--pretty=%H|%an|%ai|%f')
            print log
            for line in log.splitlines():
                line = line.split('|')
                commits.append({
                    'hash': line[0],
                    'author': line[1],
                    'date': line[2],
                    'message': line[3],
                    })
        except:
            logger.exception("Git Log Error")
        return commits
