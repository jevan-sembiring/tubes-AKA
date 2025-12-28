from flask import Flask, render_template, request
import time
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

app = Flask(__name__)

def jump_search(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    steps = 0

    while prev < n and arr[min(step, n)-1] < key:
        steps += 1
        prev = step
        step += int(math.sqrt(n))

    for i in range(prev, min(step, n)):
        steps += 1
        if arr[i] == key:
            return i, steps

    return -1, steps


def binary_search_iter(arr, left, right, key):
    steps = 0
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid, steps
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1, steps


def binary_search_rec(arr, left, right, key, steps):
    if left <= right:
        steps[0] += 1
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search_rec(arr, left, mid-1, key, steps)
        else:
            return binary_search_rec(arr, mid+1, right, key, steps)
    return -1


def exponential_iter(arr, key):
    steps = 1
    if arr[0] == key:
        return 0, steps

    i = 1
    while i < len(arr) and arr[i] <= key:
        steps += 1
        i *= 2

    _, bs_steps = binary_search_iter(arr, i//2, min(i, len(arr)-1), key)
    return -1, steps + bs_steps


def exponential_rec(arr, key):
    steps = [1]
    if arr[0] == key:
        return 0, steps[0]

    i = 1
    while i < len(arr) and arr[i] <= key:
        steps[0] += 1
        i *= 2

    binary_search_rec(arr, i//2, min(i, len(arr)-1), key, steps)
    return -1, steps[0]

@app.route("/", methods=["GET", "POST"])
def index():
    results = None

    if request.method == "POST":
        n = int(request.form["n"])
        arr = list(range(1, n+1))

        cases = {
            "Best Case": 1,
            "Average Case": n // 2,
            "Worst Case": n
        }

        results = {}

        for case, key in cases.items():
            t0 = time.perf_counter_ns()
            _, js_steps = jump_search(arr, key)
            js_time = (time.perf_counter_ns() - t0) / 1_000_000

            t0 = time.perf_counter_ns()
            _, ei_steps = exponential_iter(arr, key)
            ei_time = (time.perf_counter_ns() - t0) / 1_000_000

            t0 = time.perf_counter_ns()
            _, er_steps = exponential_rec(arr, key)
            er_time = (time.perf_counter_ns() - t0) / 1_000_000

            results[case] = [
                ("Jump Search", js_steps, js_time),
                ("Exponential Iteratif", ei_steps, ei_time),
                ("Exponential Rekursif", er_steps, er_time)
            ]

        labels = list(cases.keys())
        iter_times = [results[c][1][2] for c in labels]
        rec_times = [results[c][2][2] for c in labels]

        plt.figure()
        plt.plot(labels, iter_times, marker='o', label="Iteratif")
        plt.plot(labels, rec_times, marker='o', label="Rekursif")
        plt.legend()
        plt.title("Exponential Search: Iteratif vs Rekursif")
        plt.ylabel("Waktu (ms)")
        plt.savefig("static/exp_iter_vs_rec.png")
        plt.close()

        jump_times = [results[c][0][2] for c in labels]

        plt.figure()
        plt.plot(labels, jump_times, marker='o', label="Jump Search")
        plt.plot(labels, iter_times, marker='o', label="Exponential Iteratif")
        plt.plot(labels, rec_times, marker='o', label="Exponential Rekursif")
        plt.legend()
        plt.title("Perbandingan Semua Algoritma")
        plt.ylabel("Waktu (ms)")
        plt.savefig("static/compare_all.png")
        plt.close()

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)