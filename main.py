import areas
import system_health


def main():
    print(f"{'_'*43}")
    print('Welcome to Interaction with OS with Python')

    # Areas of shapes from areas package
    print(f"{'_' * 10} Area 0f Shapes {'_' * 17}")
    print(f'Area of triangle : {areas.triangle(5,3)}')
    print(f'Area of rectangle : {areas.rectangle(5,3)}')
    print(f'Area of circle : {areas.circle(5)}')
    print(f'Area of donut : {areas.donut(5,3)}')

    # System Health Check from system_health pacakge
    print(f"{'_' * 10} System Health Check {'_' * 12}")
    if not system_health.check_disk_usage('/') or not system_health.check_cpu_usage(1):
        print('Error')
    else:
        print('Everything is ok!')


if __name__ == '__main__':
    main()
