from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    context = {'title': 'Home'}
    return render_template('home.html', **context)


@app.route('/cloth/')
def cloth():
    context = {'title': 'Cloth'}
    return render_template('cloth.html', **context)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Shoes'}
    return render_template('shoes.html', **context)


@app.route('/cloth/jackets/')
def jackets():
    _jackets = [{'name': 'item_1',
                 'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta, accusamus.',
                 'image': url_for('static', filename='/jackets_items/item_1.jpg')},
                {'name': 'item_2',
                 'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta, accusamus.',
                 'image': url_for('static', filename='/jackets_items/item_2.jpg')},
                {'name': 'item_3',
                 'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta, accusamus.',
                 'image': url_for('static', filename='/jackets_items/item_3.jpg')}]
    context = {'title': 'Jackets',
               'jackets': _jackets}
    return render_template('clothes/jackets.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
