def collision(character, obstacle):
    if character.rect.colliderect(obstacle.rect):
        if character.direction.x > 0:
            character.rect.right = obstacle.rect.left
        elif character.direction.x < 0:
            character.rect.left = obstacle.rect.right

        if character.direction.y > 0:
            character.rect.bottom = obstacle.rect.top
        elif character.direction.y < 0:
            character.rect.top = obstacle.rect.bottom
