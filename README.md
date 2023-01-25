#nome-do-projeto
# SEE HOW PACKAGE

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)

<img src="img/show-img-processed.png" alt="Imagem processada e tópico ROS sendo publicado">

> Projeto desenvolvido com o objetivo de integrar tecnologias como a visão computacional ao ROS, visando a facilidade de adaptação. 

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [ ] Visualização Grafica dos Resultados
- [ ] Imagem Docker 
- [ ] FastApi
- [ ] Integração com Banco de Dados

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* `Ubuntu 18.04`
* `ROS Melodic`
* `Python 3.10`
* `rospy`
* `ros_numpy`
* `cv2`
* `mediapipe`
* `numpy`
* `math`
* `cv_bridge`

## 🚀 Instalando SEE HOW PACKAGE

Para instalar o SEE HOW PACKAGE, siga estas etapas:

Linux:
```
mkdir -p ws/src
cd ws/src
git clone https://github.com/nata-vito/see_how_pkg.git

cd ..
catkin_make
source devel/setup.bash
```

## ☕ Usando SEE HOW PACKAGE

Para usar SEE HOW PACKAGE, siga estas etapas:

```
roslaunch see_how_pkg see_how.launch
```

Caso você não consiga executar, certifique-se que foi realizado o `source devel/setup.bash` dentro da pasta ws. Caso não, execute o comando novamente em todas as janelas do terminal.


## 📫 Contribuindo para SEE HOW PACKAGE
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->
Para contribuir com SEE HOW PACKAGE, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

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


## 😄 Seja um dos contribuidores<br>

Quer fazer parte desse projeto? Clique [AQUI](CONTRIBUTING.md) e leia como contribuir.

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

[⬆ Voltar ao topo](#nome-do-projeto)<br>
