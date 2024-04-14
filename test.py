from src.integrations.netflix import Netflix


def test_netflix():
    manager = Netflix()
    media = manager.get_media()
    assert media is not None
    assert len(media) > 0
    assert all([media_item.show is not None for media_item in media])
    assert all([media_item.season is not None for media_item in media])
    assert all([media_item.episode is not None for media_item in media])
    pass


if __name__ == '__main__':
    test_netflix()
    pass