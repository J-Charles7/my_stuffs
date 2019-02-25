# How to install ELK Stack on a Debian distrib?
## Elasticsearch

#### Download and install the public signing key:
```shell
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
```
#### As ELK packages are signed, you need to install `apt-transport-https` so as to support this feature:
```shell
sudo apt-get install apt-transport-https
```
#### Save the repository definition to /etc/apt/sources.list.d/elastic-6.x.list:
```shell
echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
```
#### Install Elasticsearch:
```shell
sudo apt-get update && sudo apt-get install elasticsearch
```

#### Check if `elasticsearch` user is created:
```shell
sudo grep elasticsearch /etc/passwd
```

You should have this output (with different GID/UID):
```shell
elasticsearch:x:122:129::/nonexistent:/bin/false
```

#### Start `elasticsearch` service: 
```shell
sudo service elasticsearch start
```

#### Check the status of the service and make sure it is `active`:
```shell
sudo service elasticsearch status
```
#### Check that elasticsearch installation is well completed:
```shell
sudo service elasticsearch start
``` 

You should have this output:
```JSON
{
  "name" : "Cp8oag6",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "AT69_T_DTp-1qgIJlatQqA",
  "version" : {
    "number" : "6.6.1",
    "build_flavor" : "default",
    "build_type" : "zip",
    "build_hash" : "f27399d",
    "build_date" : "2016-03-30T09:51:41.449Z",
    "build_snapshot" : false,
    "lucene_version" : "7.6.0",
    "minimum_wire_compatibility_version" : "1.2.3",
    "minimum_index_compatibility_version" : "1.2.3"
  },
  "tagline" : "You Know, for Search"
}
```
