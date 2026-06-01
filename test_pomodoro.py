import unittest

import pomodoro


class PomodoroTests(unittest.TestCase):
    def test_format_time(self):
        self.assertEqual(pomodoro.format_time(0), "00:00")
        self.assertEqual(pomodoro.format_time(65), "01:05")
        self.assertEqual(pomodoro.format_time(-5), "00:00")

    def test_default_duration(self):
        args = pomodoro.parse_args([])
        self.assertEqual(pomodoro.duration_from_args(args), 25 * 60)

    def test_custom_duration(self):
        args = pomodoro.parse_args(["--minutes", "1.5"])
        self.assertEqual(pomodoro.duration_from_args(args), 90)

    def test_break_duration(self):
        args = pomodoro.parse_args(["--break", "--minutes", "99"])
        self.assertEqual(pomodoro.duration_from_args(args), 5 * 60)

    def test_rejects_non_positive_duration(self):
        args = pomodoro.parse_args(["--minutes", "0"])
        with self.assertRaises(ValueError):
            pomodoro.duration_from_args(args)


if __name__ == "__main__":
    unittest.main()
