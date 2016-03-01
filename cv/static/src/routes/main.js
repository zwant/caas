import Relay from 'react-relay';

export default class extends Relay.Route {
  static queries = {
    allCvs: () => Relay.QL`
      query {
        node(id: "Q1Y6MQ==")
      }`
  };
  static routeName = 'MainRoute';
}
