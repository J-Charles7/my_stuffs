# How to install ELK Stack on a Debian distrib?
## 1. Elasticsearch

#### 1.1. Download and install the public signing key:
```shell
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
```
#### 1.2. As ELK packages are signed, you need to install `apt-transport-https` so as to support this feature:
```shell
sudo apt-get install apt-transport-https
```
#### 1.3. Save the repository definition to /etc/apt/sources.list.d/elastic-6.x.list:
```shell
echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
```
#### 1.4. Install Elasticsearch:
```shell
sudo apt-get update && sudo apt-get install elasticsearch
```

#### 1.5. Check if `elasticsearch` user is created:
```shell
sudo grep elasticsearch /etc/passwd
```

You should have this output (with different GID/UID):
```shell
elasticsearch:x:122:129::/nonexistent:/bin/false
```

#### 1.6. Start `elasticsearch` service: 
```shell
sudo service elasticsearch start
```

#### 1.7. Check the status of the service and make sure it is `active`:
```shell
sudo service elasticsearch status
```
#### 1.8. Check that elasticsearch installation is well completed:

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

## 2. Kibana
You can follow steps [1.1](https://github.com/J-Charles7/my_stuffs/blob/master/Guides/ELK_installation.md#11-download-and-install-the-public-signing-key) to [1.3](https://github.com/J-Charles7/my_stuffs/blob/master/Guides/ELK_installation.md#13-save-the-repository-definition-to-etcaptsourceslistdelastic-6xlist)
