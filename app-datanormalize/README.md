[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.0-green.svg)](https://github.com/soichih/abcd-spec)

# app-datanormalize
application to normalize the bvalues and flip the bvecs if necessary

# Running via Docker

You can run this app anywhere that has docker engine installed.

## Build docker container

If you are not going to use the one that we've published on docker hub, you can build the container locally by git cloning this repo, and then run following command

`docker build -t app-datanormalize .`

## Create config.json

This container receives input parameter via config.json. Create something like following in your current working directory.

```
{
        "bvals": "/input/dwi.bvals",
        "bvecs": "/input/dwi.bvecs",
        "dwi": "/input/dwi.nii.gz",
        "xflip": true,
        "yflip": false,
        "zflip": false
}
```

/input is a path inside the container which we will map from our host directory. In this example, I will create a directory called testdata in my working directory.

```
mkdir testdata
# copy your dwi.bvals, dwi.bvecs, and dwi.nii.gz in to testdata
```
## Running container

Now, run docker run to run the app

```
docker run -it --rm \
    -v `pwd`/testdata:/input \
    -v `pwd`:/output \
    app-datanormalize

```

We will volume mount (-v) current working directory's testdata directory as container's /input directory, and also the current working directory as container's /output directory. /output directory is used as the working directory inside the container (which is mounted from the host's current working directory). So, by placing the config.json on the host's current working directory, container will find config.json under its /output directory.
