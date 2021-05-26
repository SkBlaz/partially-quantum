## Some minimal examples of quantum computing.

First, let's set up the token access. Here, by running

```
pip install dwave-ocean-sdk
```

And creating the profile with the API endpoint:

```
dwave config create
```
And follow the instructions.


## Testing

The first thing after a successful config is to test the API validity. Simply run

```
dwave ping
```

and inspect the output, which looks e.g., like:

```
Using endpoint: https://cloud.dwavesys.com/sapi/
Using solver: DW_2000Q_6
Submitted problem ID: aa13269d-780f-4597-bab5-54abae8402b5

Wall clock time:
 * Solver definition fetch: 1524.460 ms
 * Problem submit and results fetch: 2312.535 ms
 * Total: 3836.995 ms

QPU timing:
 * post_processing_overhead_time = 842 us
 * qpu_access_overhead_time = 1808 us
 * qpu_access_time = 11012 us
 * qpu_anneal_time_per_sample = 20 us
 * qpu_delay_time_per_sample = 21 us
 * qpu_programming_time = 10773 us
 * qpu_readout_time_per_sample = 198 us
 * qpu_sampling_time = 239 us
 * total_post_processing_time = 842 us
```

## Finding the available solvers

```
dwave solvers
```
yields the list of all solvers!