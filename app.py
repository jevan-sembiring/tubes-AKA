from flask import Flask, render_template, request
import time, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# ---------------- ALGORITMA ----------------

def jump_search(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    steps = 0

    while prev < n and arr[min(step, n)-1] < key:
        steps += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, steps

    for i in range(prev, min(step, n)):
        steps += 1
        if arr[i] == key:
            return i, steps
    return -1, steps


def binary_search_recursive(arr, l, r, key, steps):
    if l <= r:
        mid = (l + r) // 2
        steps[0] += 1
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binary_search_recursive(arr, l, mid-1, key, steps)
        else:
            return binary_search_recursive(arr, mid+1, r, key, steps)
    return -1


def exponential_iterative(arr, key):
    steps = 1
    n = len(arr)
    if arr[0] == key:
        return 0, steps

    i = 1
    while i < n and arr[i] <= key:
        steps += 1
        i *= 2

    bs_steps = [steps]
    binary_search_recursive(arr, i//2, min(i, n-1), key, bs_steps)
    return -1, bs_steps[0]


def exponential_recursive(arr, key):
    steps = [1]
    binary_search_recursive(arr, 0, len(arr)-1, key, steps)
    return -1, steps[0]

# ---------------- ROUTE ----------------

@app.route("/", methods=["GET", "POST"])
def index():
    results = None

    if request.method == "POST":
        n = int(request.form["n"])
        arr = list(range(1, n+1))

        cases = {
            "Best Case": 1,
            "Average Case": n//2,
            "Worst Case": n
        }

        results = []

        for case, key in cases.items():
            # Jump
            t0 = time.perf_counter_ns()
            _, js = jump_search(arr, key)
            jt = (time.perf_counter_ns() - t0)/1e6

            # Exponential Iteratif
            t0 = time.perf_counter_ns()
            _, ei = exponential_iterative(arr, key)
            eit = (time.perf_counter_ns() - t0)/1e6

            # Exponential Rekursif
            t0 = time.perf_counter_ns()
            _, er = exponential_recursive(arr, key)
            ert = (time.perf_counter_ns() - t0)/1e6

            results.append({
                "case": case,
                "jump": (js, jt),
                "exp_it": (ei, eit),
                "exp_rec": (er, ert)
            })

        # ---------------- GRAFIK ----------------
        labels = [r["case"] for r in results]

        # Grafik 1: Exponential Iteratif vs Rekursif
        plt.figure()
        plt.plot(labels, [r["exp_it"][1] for r in results], label="Exponential Iteratif")
        plt.plot(labels, [r["exp_rec"][1] for r in results], label="Exponential Rekursif")
        plt.legend()
        plt.ylabel("Waktu (ms)")
        plt.title("Exponential Iteratif vs Rekursif")
        plt.savefig("static/exp_compare.png")
        plt.close()

        # Grafik 2: Jump vs Exponential Iteratif
        plt.figure()
        plt.plot(labels, [r["jump"][1] for r in results], label="Jump Search")
        plt.plot(labels, [r["exp_it"][1] for r in results], label="Exponential Iteratif")
        plt.legend()
        plt.ylabel("Waktu (ms)")
        plt.title("Jump Search vs Exponential Iteratif")
        plt.savefig("static/jump_vs_exp.png")
        plt.close()

    return render_template("index.html", results=results)

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
