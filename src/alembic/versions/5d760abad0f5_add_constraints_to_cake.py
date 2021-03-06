"""Add constraints to cake

Revision ID: 5d760abad0f5
Revises: ae9f0a0b54f4
Create Date: 2021-11-09 18:12:10.644359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d760abad0f5'
down_revision = 'ae9f0a0b54f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cake', sa.Column('name', sa.String(), nullable=True))
    op.add_column('cake', sa.Column('comment', sa.String(), nullable=True))
    op.add_column('cake', sa.Column('image_url', sa.String(), nullable=True))
    op.add_column('cake', sa.Column('yum_factor', sa.Integer(), nullable=True))
    op.drop_index('ix_cake_description', table_name='cake')
    op.drop_index('ix_cake_title', table_name='cake')
    op.create_index(op.f('ix_cake_comment'), 'cake', ['comment'], unique=False)
    op.create_index(op.f('ix_cake_image_url'), 'cake', ['image_url'], unique=False)
    op.create_index(op.f('ix_cake_name'), 'cake', ['name'], unique=False)
    op.create_index(op.f('ix_cake_yum_factor'), 'cake', ['yum_factor'], unique=False)
    op.drop_column('cake', 'title')
    op.drop_column('cake', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cake', sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('cake', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_cake_yum_factor'), table_name='cake')
    op.drop_index(op.f('ix_cake_name'), table_name='cake')
    op.drop_index(op.f('ix_cake_image_url'), table_name='cake')
    op.drop_index(op.f('ix_cake_comment'), table_name='cake')
    op.create_index('ix_cake_title', 'cake', ['title'], unique=False)
    op.create_index('ix_cake_description', 'cake', ['description'], unique=False)
    op.drop_column('cake', 'yum_factor')
    op.drop_column('cake', 'image_url')
    op.drop_column('cake', 'comment')
    op.drop_column('cake', 'name')
    # ### end Alembic commands ###
