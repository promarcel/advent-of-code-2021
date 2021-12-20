from rich import print


def get_input():
    with open('input.txt') as input_txt:
        enhancement_key = [0 if c == '.' else 1 for c in next(input_txt).strip()]
        next(input_txt)
        image = []
        for line in input_txt:
            image_row = [0 if c == '.' else 1 for c in line.strip()]
            image.append(image_row)
    return image, enhancement_key


def enhance_once(image, enhancement_key):
    height = len(image)
    width = len(image[0])

    if image[0][0] == 0:
        border = enhancement_key[0]
    else:
        border = enhancement_key[-1]

    resolution = [[border] * width]

    for i in range(1, height - 1):
        resolution_row = [border]
        for j in range(1, width - 1):
            index = (image[i - 1][j - 1] * 256 + image[i - 1][j] * 128 + image[i - 1][j + 1] * 64 +
                     image[i][j - 1] * 32 + image[i][j] * 16 + image[i][j + 1] * 8 +
                     image[i + 1][j - 1] * 4 + image[i + 1][j] * 2 + image[i + 1][j + 1])
            resolution_row.append(enhancement_key[index])
        resolution_row.append(border)
        resolution.append(resolution_row)

    resolution.append([border] * width)

    return resolution


def enhance(image, n, enhancement_key):
    width = len(image[0])
    resolution = [[0] * (width + 2 * n + 2)] * (n + 1)

    for row in image:
        resolution.append([0] * (n + 1) + row + [0] * (n + 1))
    resolution.extend([[0] * (width + 2 * n + 2)] * (n + 1))

    for _ in range(n):
        resolution = enhance_once(resolution, enhancement_key)

    return resolution


def part_1(image, enhancement_key):
    part_1 = enhance(image, 2, enhancement_key)
    part_1 = sum([sum(row) for row in part_1])
    return part_1


def part_2(image, enhancement_key):
    part_2 = enhance(image, 50, enhancement_key)
    part_2 = sum([sum(row) for row in part_2])
    return part_2


if __name__ == "__main__":
    image, enhancement_key = get_input()

    part_1 = part_1(image, enhancement_key)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(image, enhancement_key)
    print(f"Puzzle Part 2: {part_2}")
