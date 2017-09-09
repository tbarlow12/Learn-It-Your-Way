import React from "react";
import Dropzone from 'react-dropzone'

export default class home extends React.Component {

  constructor(props) {
    super(props);
    this.state = {greeting: 'Hello ' + this.props.name};

    this.handleSubmit= this.handleSubmit.bind(this);
    this.onClick= this.onClick.bind(this);
    this.changeState= this.changeState.bind(this);
  }

  onDrop(acceptedFiles) {
    this.setState({acceptedFiles});
  }

  handleSubmit() {
    e.preventDefault();
    const {acceptedFiles} = this.state;

    if (acceptedFiles != null) {
      formData.append('file', acceptedFiles[acceptedFiles - 1]);
    }
    this.setState({requesting: true});

    // Request.profile.update(formData)
    //   .then(res => {
    //     console.log('ProfileBuilder updateProfile', res);
    //     AppModel.cacheProfile(res);
    //     this.props.updateAvatar(res.profile.avatarUrl);
    //     routeHandler.redirectTo("/profile");
    //   })
    //   .catch(err => {
    //     this.setState({err: err.message, requesting: false});
    //   });
  }

  onClick() {

  }

  changeState() {

  }

  componentWillReceiveProps() {

  }

  componentDidMount() {

  }

  render() {
    return (
      <div className="main">
        Home Test
        <div className="main-section">
          <Dropzone className="img-drop" ref="dropzone" onDrop={this.onDrop.bind(this)}>
            <button>Upload CSV Data File</button>
          </Dropzone>
        </div>
      </div>

    )

  }

}