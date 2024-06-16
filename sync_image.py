# coding:utf-8
import subprocess, os
def get_filename():
    with open("images.txt", "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines if line.strip()]
        return lines


def pull_image():
    map_list= get_filename()
    print("name_list:", map_list)
    subprocess.call("docker login -u zou.juny@gmail.com -p 2wjddls@ali registry.cn-hangzhou.aliyuncs.com", shell=True)
    new_name_prefix = "registry.cn-hangzhou.aliyuncs.com/hexai/"
    for map_item in map_list:
        split_items = map_item.split("|")
        if len(split_items) != 2:
            print("split_items:{} len != 2".format(split_items))
            continue

        src_repo = split_items[0]
        dst_repo_name = split_items[1]
        src_repo_tag = src_repo.split(":")[-1]

        name = src_repo
        new_name = new_name_prefix + dst_repo_name + ":" + src_repo_tag
        cmd = "docker tag {0} {1}".format(name, new_name)
        print(cmd)
        subprocess.call("docker pull {}".format(name), shell=True)
        subprocess.run(["docker", "tag", name, new_name])
        subprocess.call("docker push {}".format(new_name), shell=True)

       
if __name__ == "__main__":
    pull_image()
