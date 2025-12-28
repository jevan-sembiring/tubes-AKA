from flask import Flask, render_template, request
import time
import math
import matplotlib
import matplotlib.pyplot as plt
import os
matplotlib.use("Agg")

app = Flask(__name__)

def jump_search(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    steps = 0

    while prev < n and arr[min(step, n) - 1] < key:
        steps += 1
        prev = step
        step += int(math.sqrt(n))

    for i in range(prev, min(step, n)):
        steps += 1
        if arr[i] == key:
            return steps
    return steps


def binary_search_recursive(arr, left, right, key, steps):
    if left > right:
        return
    steps[0] += 1
    mid = (left + right) // 2
    if arr[mid] == key:
        return
    elif key < arr[mid]:
        binary_search_recursive(arr, left, mid - 1, key, steps)
    else:
        binary_search_recursive(arr, mid + 1, right, key, steps)


def exponential_search_iterative(arr, key):
    steps = 1
    if arr[0] == key:
        return steps

    i = 1
    n = len(arr)
    while i < n and arr[i] <= key:
        steps += 1
        i *= 2

    left = i // 2
    right = min(i, n - 1)
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == key:
            break
        elif key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return steps


def exponential_search_recursive(arr, key):
    if arr[0] == key:
        return 1

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        n = int(request.form["n"])
        arr = list(range(1, n + 1))

        cases = {
            "Best Case": 1,
            "Average Case": n // 2,
            "Worst Case": n
        }

        results = {}

        for case, key in cases.items():
            t0 = time.perf_counter_ns()
            _, js = jump_search(arr, key)
            jt = (time.perf_counter_ns() - t0)/1e6

            t0 = time.perf_counter_ns()
            _, ei = exponential_iterative(arr, key)
            eit = (time.perf_counter_ns() - t0)/1e6

            t0 = time.perf_counter_ns()
            _, er = exponential_recursive(arr, key)
            ert = (time.perf_counter_ns() - t0)/1e6

            results[case] = [
                ("Jump Search", js_steps, js_time),
                ("Exponential Iteratif", ei_steps, ei_time),
                ("Exponential Rekursif", er_steps, er_time)
            ]

        labels = list(cases.keys())
        iter_times = [results[c][1][2] for c in labels]
        rec_times = [results[c][2][2] for c in labels]

        plt.figure()
        plt.plot(labels, ei_times, marker="o", label="Exponential Iteratif")
        plt.plot(labels, er_times, marker="o", label="Exponential Rekursif")
        plt.title("Exponential Search: Iteratif vs Rekursif")
        plt.ylabel("Waktu (ms)")
        plt.legend()
        plt.savefig("static/exp_compare.png")
        plt.close()

        jump_times = [results[c][0][2] for c in labels]

        plt.figure()
        plt.plot(labels, js_times, marker="o", label="Jump Search")
        plt.plot(labels, ei_times, marker="o", label="Exponential Iteratif")
        plt.title("Jump Search vs Exponential Iteratif")
        plt.ylabel("Waktu (ms)")
        plt.legend()
        plt.savefig("static/jump_vs_exp.png")
        plt.close()

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
