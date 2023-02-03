# SEE HOW PACKAGE

<center>

![GitHub python version](https://img.shields.io/badge/Python-3.9.0-green?style=flat-square&logo=python)
![GitHub python version](https://img.shields.io/badge/Python-2.7.15-green?style=flat-square&logo=python)
![GitHub ros version](https://img.shields.io/badge/ROS-Melodic-blue?style=flat-square&logo=ros)
![GitHub ubuntu version](https://img.shields.io/badge/Ubuntu-18.04-orange?style=flat-square&logo=ubuntu)
![Bitbucket docker](https://img.shields.io/badge/Docker-gray?style=flat-square&logo=docker)
![Bitbucket nvidia container toolkit](https://img.shields.io/badge/NVIDIA_Container_Toolkit-gray?style=flat-square&logo=nvidia)
![Bitbucket opencv](https://img.shields.io/badge/opencv-blue?style=flat-square&logo=opencv)

</center>


<img src="img/show-img-processed.png" alt="Image processed and ROS topic being published">

> Project developed with the objective of integrating technologies such as computer vision to the ROS, aiming for ease of adaptation. 

### Adjustments and improvements

The project is still under development and the next updates will focus on the following tasks:

- [ ] Graphical View of the Results
- [x] Docker Image
- [ ] FastApi
- [ ] Database Integration
---
## 💻 Prerequisites

Before you begin, check that you have met the following requirements:
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* `Ubuntu 18.04`
* `ROS Melodic`
* `Python 3.10`
* `rospy`
* `ros_numpy`
* `cv2`
* `mediapipe`
* `numpy`
* `cv_bridge`
---
## 🚀 Installing SEE HOW PACKAGE

To install the SEE HOW PACKAGE, follow these steps:

Linux:
```
mkdir -p ws/src
cd ws/src
git clone https://github.com/nata-vito/see_how_pkg.git

cd ..
catkin_make
source devel/setup.bash
```
---
Docker:

- Requirements for the proper functioning of the Image

  - First of all, install the NVIDIA Container Toolkit and its drivers following the official Nvidia documentation. NVIDIA Documentation: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker
  
---
### Running the image

After that, run the commands below.

  - Command to download the image: 
      
      ```docker pull natavitorino/cuda-ros:<tag version here>```

  - Command to release screen access:

      ```xhost +local:docker```

  - Command to run the contianer with privileges:
      
      ```docker run -it --rm --privileged --net=host --env=NVIDIA_VISIBLE_DEVICES=all --env=NVIDIA_DRIVER_CAPABILITIES=all --env=DISPLAY --env=QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix --gpus all natavitorino/cuda-ros:<tag version here> bash```


---
  - Tags:

      ```1.0``` - Version without Yolo support

      ```1.1``` - Version with Yolo support
---

## ☕ Using SEE HOW PACKAGE

To use SEE HOW PACKAGE, follow these steps:

```
roslaunch see_how_pkg see_how.launch
```

If you can't run it, make sure you have `source devel/setup.bash` inside the ws folder. If not, run the command again in all terminal windows. 

Modify the shebang of the components to be copied correctly, the current shebangs are set to run on the official docker image of the project.

---
## 📫 Contributing to SEE HOW PACKAGE
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->
To contribute to SEE HOW PACKAGE, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <nome_branch>`.
3. Make your changes and confirm them: `git commit -m '<mensagem_commit>'`
4. Send to original branch: `git push origin <nome_do_projeto> / <local>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [how to create a pull request].(https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

---
## 🤝 Collaborators

We thank the following people who contributed to this project:

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/64169072?v=4" width="100px;" alt="Foto do Natanael Vitorino no GitHub"/><br>
        <sub>
          <b>Natanael Vitorino</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---
## 😄 Be one of the contributors<br>

Want to be part of this project? Click [HERE](CONTRIBUTING.md) and read how to contribute.
---
## 📝 License

This project is under license. See the file [LICENSE](LICENSE.md) for more details.

[⬆ Back to top](#SEE-HOW-PACKAGE)<br>
