from django.shortcuts import render
from django.http import Http404

def home(request):
    return render(request, 'rental/index.html')

def about(request):
    return render(request, 'rental/about.html')

def services(request):
    return render(request, 'rental/services.html')

def pricing(request):
    return render(request, 'rental/pricing.html')

def cars(request):
    return render(request, 'rental/car.html')

def car_single(request, car_id):
    # Hardcoded car data
    cars = {
        1: {
            'id': 1,
            'name': 'Dacia Duster',
            'brand': 'Dacia',
            'image': 'images/dacia.jpeg',
            'mileage': 'less than 60,000 km',
            'transmission': 'Manual',
            'seats': '5 Adults',
            'luggage': '4 Bags',
            'fuel': 'Diesel',
            'description': 'The Dacia Duster is a versatile SUV designed for both city driving and off-road adventures in Tunisia.',
            'description_extra': 'With high ground clearance and a robust build, it’s perfect for exploring the Tunisian countryside, from the beaches of Hammamet to the dunes of the Sahara.'
        },
        2: {
            'id': 2,
            'name': 'Volkswagen Virtus',
            'brand': 'Volkswagen',
            'image': 'images/Volkswagen-Vertus.jpg',
            'mileage': 'less than 80,000 km km',
            'transmission': 'Automatic',
            'seats': '5 Adults',
            'luggage': '3 Bags',
            'fuel': 'Petrol',
            'description': 'The Volkswagen Virtus is a stylish and comfortable sedan ideal for city trips and business travel in Tunisia.',
            'description_extra': 'Equipped with modern amenities like touchscreen infotainment, it ensures a smooth and enjoyable ride through Tunis or Sousse.'
        },
      
    }
    
    car = cars.get(car_id)
    if not car:
        raise Http404("Car not found")
    
    return render(request, 'rental/car-single.html', {'car': car})

def blog(request):
    # Hardcoded blog data
    blogs = [
        {
            'id': 1,
            'image': 'images/image_1.jpg',
            'date': 'Oct. 29, 2019',
            'author': 'Admin',
            'comments': 3,
            'title': 'Why Lead Generation is Key for Business Growth',
            'excerpt': 'A small river named Duden flows by their place and supplies it with the necessary regelialia.'
        },
        {
            'id': 2,
            'image': 'images/image_2.jpg',
            'date': 'Oct. 29, 2019',
            'author': 'Admin',
            'comments': 3,
            'title': 'Top Tips for Renting a Car',
            'excerpt': 'Discover the best strategies for renting a car to ensure a smooth experience.'
        },
        {
            'id': 3,
            'image': 'images/image_3.jpg',
            'date': 'Oct. 29, 2019',
            'author': 'Admin',
            'comments': 3,
            'title': 'The Future of Car Rentals',
            'excerpt': 'Explore how technology is shaping the future of the car rental industry.'
        },
        {
            'id': 4,
            'image': 'images/image_4.jpg',
            'date': 'Oct. 29, 2019',
            'author': 'Admin',
            'comments': 3,
            'title': 'How to Save Money on Car Rentals',
            'excerpt': 'Learn practical tips to get the best deals on your next car rental.'
        },
        {
            'id': 5,
            'image': 'images/image_5.jpg',
            'date': 'Oct. 29, 2019',
            'author': 'Admin',
            'comments': 3,
            'title': 'Choosing the Right Car for Your Trip',
            'excerpt': 'Find out how to select the perfect vehicle for your travel needs.'
        },
        {
            'id': 6,
            'image': 'images/image_6.jpg',
            'date': 'Oct. 29, 2019',
            'author': 'Admin',
            'comments': 3,
            'title': 'Maintaining Your Rental Car',
            'excerpt': 'Tips for keeping your rental car in top condition during your trip.'
        }
    ]
    return render(request, 'rental/blog.html', {'blogs': blogs})

def blog_single(request, blog_id):
    # Hardcoded blog data
    blogs = {
        1: {
            'id': 1,
            'title': 'It is a long established fact a reader be distracted',
            'image_1': 'images/image_7.jpg',
            'image_2': 'images/image_8.jpg',
            'content_1': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis, eius mollitia suscipit, quisquam doloremque distinctio perferendis et doloribus unde architecto optio laboriosam porro adipisci sapiente officiis nemo accusamus ad praesentium? Esse minima nisi et. Dolore perferendis, enim praesentium omnis, iste doloremque quia officia optio deserunt molestiae voluptates soluta architecto tempora.',
            'content_2': 'Molestiae cupiditate inventore animi, maxime sapiente optio, illo est nemo veritatis repellat sunt doloribus nesciunt! Minima laborum magni reiciendis qui voluptate quisquam voluptatem soluta illo eum ullam incidunt rem assumenda eveniet eaque sequi deleniti tenetur dolore amet fugit perspiciatis ipsa, odit. Nesciunt dolor minima esse vero ut ea, repudiandae suscipit!',
            'subtitle': 'Creative WordPress Themes',
            'content_3': 'Temporibus ad error suscipit exercitationem hic molestiae totam obcaecati rerum, eius aut, in. Exercitationem atque quidem tempora maiores ex architecto voluptatum aut officia doloremque. Error dolore voluptas, omnis molestias odio dignissimos culpa ex earum nisi consequatur quos odit quasi repellat qui officiis reiciendis incidunt hic non? Debitis commodi aut, adipisci.',
            'content_4': 'Quisquam esse aliquam fuga distinctio, quidem delectus veritatis reiciendis. Nihil explicabo quod, est eos ipsum. Unde aut non tenetur tempore, nisi culpa voluptate maiores officiis quis vel ab consectetur suscipit veritatis nulla quos quia aspernatur perferendis, libero sint. Error, velit, porro. Deserunt minus, quibusdam iste enim veniam, modi rem maiores.',
            'content_5': 'Odit voluptatibus, eveniet vel nihil cum ullam dolores laborum, quo velit commodi rerum eum quidem pariatur! Quia fuga iste tenetur, ipsa vel nisi in dolorum consequatur, veritatis porro explicabo soluta commodi libero voluptatem similique id quidem? Blanditiis voluptates aperiam non magni. Reprehenderit nobis odit inventore, quia laboriosam harum excepturi ea.',
            'content_6': 'Adipisci vero culpa, eius nobis soluta. Dolore, maxime ullam ipsam quidem, dolor distinctio similique asperiores voluptas enim, exercitationem ratione aut adipisci modi quod quibusdam iusto, voluptates beatae iure nemo itaque laborum. Consequuntur et pariatur totam fuga eligendi vero dolorum provident. Voluptatibus, veritatis. Beatae numquam nam ab voluptatibus culpa, tenetur recusandae!',
            'content_7': 'Voluptas dolores dignissimos dolorum temporibus, autem aliquam ducimus at officia adipisci quasi nemo a perspiciatis provident magni laboriosam repudiandae iure iusto commodi debitis est blanditiis alias laborum sint dolore. Dolores, iure, reprehenderit. Error provident, pariatur cupiditate soluta doloremque aut ratione. Harum voluptates mollitia illo minus praesentium, rerum ipsa debitis, inventore?',
            'tags': ['Life', 'Sport', 'Tech', 'Travel'],
            'author': 'George Washington',
            'author_bio': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus itaque, autem necessitatibus voluptate quod mollitia delectus aut, sunt placeat nam vero culpa sapiente consectetur similique, inventore eos fugit cupiditate numquam!',
            'comments': 6,
            'comments_data': [
                {
                    'author': 'John Doe',
                    'date': 'Oct. 29, 2019 at 1:21pm',
                    'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?',
                    'replies': []
                },
                {
                    'author': 'John Doe',
                    'date': 'Oct. 29, 2019 at 1:21pm',
                    'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?',
                    'replies': [
                        {
                            'author': 'John Doe',
                            'date': 'Oct. 29, 2019 at 1:21pm',
                            'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?',
                            'replies': [
                                {
                                    'author': 'John Doe',
                                    'date': 'Oct. 29, 2019 at 1:21pm',
                                    'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?'
                                }
                            ]
                        }
                    ]
                },
                {
                    'author': 'John Doe',
                    'date': 'Oct. 29, 2019 at 1:21pm',
                    'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur quidem laborum necessitatibus, ipsam impedit vitae autem, eum officia, fugiat saepe enim sapiente iste iure! Quam voluptas earum impedit necessitatibus, nihil?',
                    'replies': []
                }
            ]
        }
    }
    
    blog = blogs.get(blog_id)
    if not blog:
        raise Http404("Blog not found")
    
    # Recent blogs for sidebar
    recent_blogs = [
        {
            'id': 1,
            'image': 'images/image_1.jpg',
            'title': 'Why Lead Generation is Key for Business Growth',
            'date': 'Oct. 29, 2019',
            'author': 'Admin',
            'comments': 19
        },
        {
            'id': 2,
            'image': 'images/image_2.jpg',
            'title': 'Top Tips for Renting a Car',
            'date': 'Oct. 29, 2019',
            'author': 'Admin',
            'comments': 19
        },
        {
            'id': 3,
            'image': 'images/image_3.jpg',
            'title': 'The Future of Car Rentals',
            'date': 'Oct. 29, 2019',
            'author': 'Admin',
            'comments': 19
        }
    ]
    
    return render(request, 'rental/blog-single.html', {'blog': blog, 'recent_blogs': recent_blogs})

def contact(request):
    return render(request, 'rental/contact.html')