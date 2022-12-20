from deploy_changed_workers import detect_workers_changed


def test_one_worker():
    all_changes = " workers/worker-1/another-file.txt red_herring.txt"
    workers = detect_workers_changed(all_changes)
    assert set(workers) == set(["worker-1"])


def test_two_workers():
    all_changes = " workers/worker-1/another-file.txt workers/worker-2/worker-2-file.txt"
    workers = detect_workers_changed(all_changes)
    assert set(workers) == set(["worker-1", "worker-2"])


def test_error_case():
    all_changes = "workers/file1.txt workers/file2.txt nothing_at_all"
    workers = detect_workers_changed(all_changes)
    assert set(workers) == set()
