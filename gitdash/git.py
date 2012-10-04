import subprocess
import logging

logger = logging.getLogger(__name__)


class Git(object):
    def __init__(self, path):
        self.path = path

    def run(self, *args):
        command = ['git'] + list(args)
        logger.info(' '.join(command))
        output = subprocess.check_output(
            command,
            cwd=self.path,
            )
        return output

    def log(self, branch):
        commits = []
        try:
            log = self.run('log', '-n', '10', '--pretty=%H|%an|%ai|%f', branch)
            for line in log.splitlines():
                logger.debug(line)
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

    def head(self):
        try:
            head = self.run('rev-parse', 'HEAD')
            logger.info('HEAD:%s', head)
            return head.strip()
        except:
            return ''
