from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest


def test_reading_plan_group_news():
    pass
    reading = ReadingPlanService()
    with pytest.raises(ValueError):
        reading.group_news_for_available_time(0)


# def test_group_news_for_available_time_zero_available_time(self):
#     with self.assertRaises(ValueError):
#         ReadingPlanService.group_news_for_available_time(0)


# def test_group_news_for_available_time_all_readable(self):
#     news = [
#         {"title": "News 1", "reading_time": 1},
#         {"title": "News 2", "reading_time": 2},
#         {"title": "News 3", "reading_time": 3},
#     ]
#     mock_db_news_proxy = (return_value=news)
#     with patch(
#         "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
#         mock_db_news_proxy,
#     ):
#         result = ReadingPlanService.group_news_for_available_time(10)
#         assert result == {
#             "readable": [
#                 {
#                     "unfilled_time": 6,
#                     "chosen_news": [
#                         ("News 1", 1),
#                         ("News 2", 2),
#                         ("News 3", 3),
#                     ],
#                 }
#             ],
#             "unreadable": [],
#         }


# def test_group_news_for_available_time_all_unreadable(self):
#     news = [
#         {"title": "News 1", "reading_time": 2},
#         {"title": "News 2", "reading_time": 2},
#         {"title": "News 3", "reading_time": 3},
#     ]
#     mock_db_news_proxy = MagicMock(return_value=news)
#     with patch(
#         "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
#         mock_db_news_proxy,
#     ):
#         result = ReadingPlanService.group_news_for_available_time()
#         assert result == {
#             "readable": [],
#             "unreadable": [
#                 ("News 1", 2),
#                 ("News 2", 2),
#                 ("News 3", 3),
#             ],
#         }


# def test_group_news_for_available_time_mixed(self):
#     news = [
#         {"title": "News 1", "reading_time": 1},
#         {"title": "News 2", "reading_time": 2},
#         {"title": "News 3", "reading_time": 3},
#         {"title": "News 4", "reading_time": 4},
#         {"title": "News 5", "reading_time": 5},
#     ]
#     mock_db_news_proxy = MagicMock(return_value=news)
#     with patch(
#         "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
#         mock_db_news_proxy,
#     ):
#         result = ReadingPlanService.group_news_for_available_time(10)
#         assert result == {
#             "readable": [
#                 {
#                     "unfilled_time": 6,
#                     "chosen_news": [
#                         ("News 1", 1),
#                         ("News 2", 2),
#                         ("News 3", 3),
#                     ],
#                 },
#                 {
#                     "unfilled_time": 2,
#                     "chosen_news": [("News 4", 4)],
#                 },
#             ],
#             "unreadable": [("News 5", 5)],
#         }
