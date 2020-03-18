Description
--------------------

[Locust][1] is a modern load testing framework written in `Python`.
By default, `Locust` will run over just single core, regardless of how many core your environment has.

However, if you expect Locust to make heavy-traffic, single-core could be not enough.

In order to take advanage of multi-core with `Locust`.
You should run [Locust distributed][2].


For ease of running `Locust distributed`, This project uses [docker swarm][3] consisting of a `Locust` master and slaves.
The number of slave could be set by environment variable `NUM_OF_SLAVE`.

Usually you will set it as many as the number of core which your environment has.


[1]: https://locust.io
[2]: https://docs.locust.io/en/stable/running-locust-distributed.html
[3]: https://docs.docker.com/engine/swarm/

Locust file
--------------------
In order to define test user activity(kind of test scenario),
You should implement `./locust/locustfile.py` as you want.

For more detail, reference [here][4].

[4]: https://docs.locust.io/en/stable/writing-a-locustfile.html


Deployment
--------------------

1. Initialize project.
```
$ ./init.sh
```

2. Set environment variable
```
$ vi set-env.sh
export NUM_OF_SLAVE=''
export ATTACKED_HOST=''

$ source set-env.sh

```

3. Get in swarm mode

```
$ docker swarm init
```

4. Remove swarm network before running, if there is
```
$ docker network rm `docker network ls --quiet --filter name=locust_swarm_network`
```

5. Run(or Update) swarm cluster
```
$ docker stack deploy -c docker-compose.yml locust
```

6. Check tasks
```
$ docker stack ps locust
```

Stop swarm cluster
--------------------
```
$ docker stack rm locust
```

Log
--------------------
```
# For locust master service
$ docker service logs locust_master

# For locust slave service
$ docker service logs locust_slave
```
