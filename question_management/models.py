from django.db import models
from django.db.models import Max
from django.utils.text import slugify

from assesment_management.models import Assesment


class Question(models.Model):

    assessment = models.ForeignKey(
        Assesment,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    question_text = models.TextField()

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    explanation = models.TextField(
        blank=True,
        null=True
    )

    marks = models.PositiveIntegerField(default=1)

    order = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Question sequence within the assessment"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

        # Assign order only when creating a new question
        if self._state.adding:

            last_order = Question.objects.filter(
                assessment=self.assessment
            ).aggregate(
                max_order=Max("order")
            )["max_order"]

            self.order = (last_order or 0) + 1

        # Generate slug automatically
        if not self.slug:

            slug_text = slugify(self.question_text)[:180] or "question"

            self.slug = f"{slug_text}-{self.assessment_id}-{self.order}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.assessment.title} - Question {self.order}"

    class Meta:
        ordering = ["order"]
        unique_together = ["assessment", "order"]