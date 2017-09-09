var $ = require('jquery');


export default class header extends React.Component {

  constructor(props) {
    super(props);
    this.state = {greeting: 'Hello ' + this.props.name};

    this.handleSubmit= this.this.handleSubmit.bind(this);
    this.onClick= this.this.onClick.bind(this);
    this.changeState= this.this.changeState.bind(this);
  }

  handleSubmit() {
    $.get(window.location.href + 'send', (data) => {
      console.log(data);
      this.changeState(data);
    });
  }

  retrieveData() {
    $.get(window.location.href + 'retrieve', (data) => {
      console.log(data);
      this.changeState(data);
    });
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
      <div>

      </div>

    )

  }

}