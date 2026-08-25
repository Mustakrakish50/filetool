import unittest
from pathlib import Path
import tempfile
import shutil
from file_ops import list_files, copy_file, move_file, delete_file

class TestFileOps(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.file_path = Path(self.test_dir) / "test.txt"
        self.file_path.write_text("test content")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_list_files(self):
        files = list_files(self.test_dir)
        self.assertIn(self.file_path, files)

    def test_copy_file(self):
        dest = Path(self.test_dir) / "backup"
        dest.mkdir()
        copy_file(str(self.file_path), str(dest))
        self.assertTrue((dest / "test.txt").exists())

    def test_move_file(self):
        dest = Path(self.test_dir) / "archive"
        dest.mkdir()
        move_file(str(self.file_path), str(dest))
        self.assertTrue((dest / "test.txt").exists())
        self.assertFalse(self.file_path.exists())

    def test_delete_file(self):
        delete_file(str(self.file_path), confirm=False)
        self.assertFalse(self.file_path.exists())

if __name__ == "__main__":
    unittest.main()
