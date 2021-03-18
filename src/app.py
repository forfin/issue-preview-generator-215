import os
from preview_generator.manager import PreviewManager

def test_problem():
    CUR_DIR = os.path.dirname(os.path.realpath(__file__))
    CACHE_PATH = '/tmp/cache'
    PROBLEM_FILE = CUR_DIR + '/problem.ai'

    manager = PreviewManager(CACHE_PATH, create_folder=True)
    output = manager.get_jpeg_preview(file_path=PROBLEM_FILE, height=512, width=512, force=True)
    print(output)

if __name__ == "__main__":
    test_problem()