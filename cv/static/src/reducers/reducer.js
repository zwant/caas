const initialState = {};

export default function Reducer(state = initialState, action) {
    switch (action.type) {
        case 'SOME_ACTION':
            return Object.assign({}, state, {
                isFetching: true
            });
        default:
            return state;
  }
}
