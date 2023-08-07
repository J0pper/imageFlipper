import pygame


class Imageclass:
    def __init__(self, screen, img, flip):
        self.screen = screen
        self.screenWidth = self.screen.get_size()[0]
        self.screenHeight = self.screen.get_size()[1]

        self.image = pygame.image.load(img)
        self.imgWidth = self.image.get_width()
        self.imgHeight = self.image.get_height()

        self.flip = flip
        self.scaledImage = self.scale_image()

        self.subsurfacedImageList = self.image_cutter()
        self.inverseImageList = self.subsurfacedImageList[::-1]

    def scale_image(self):
        tempScaledImg = pygame.transform.scale_by(self.image, 0.25)
        self.imgWidth = tempScaledImg.get_width()
        self.imgHeight = tempScaledImg.get_height()
        return tempScaledImg

    def image_cutter(self):
        subsurfacedImageList = []
        for x in range(self.imgWidth):
            imgSlice = self.scaledImage.subsurface(x, 0, 1, self.imgHeight)
            subsurfacedImageList.append(imgSlice)
        return subsurfacedImageList

    def draw(self):

        #self.screen.blit(self.scaledImage, (self.screenWidth / 2 - self.imgWidth / 2, self.screenHeight / 6))

        if self.flip:
            for y, img in enumerate(self.inverseImageList):
                self.screen.blit(self.inverseImageList[y-1], (y + (self.screenWidth - self.imgWidth) / 2, self.screenHeight / 6))
        else:
            for y, img in enumerate(self.subsurfacedImageList):
                self.screen.blit(self.subsurfacedImageList[y-1], (y + (self.screenWidth - self.imgWidth) / 2, self.screenHeight / 6))
