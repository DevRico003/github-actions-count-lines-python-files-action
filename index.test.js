const log = console.log;

beforeEach(() => {
    console.log = jest.fn();
});

afterEach(() => {
    console.log = log;
});

test('prints "Hello, World!"', () => {
    require('./index');
    expect(console.log).toHaveBeenCalledWith("Hello, World!");
});