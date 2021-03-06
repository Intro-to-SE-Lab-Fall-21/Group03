"""empty message

Revision ID: b1aeb4e245d6
Revises: 
Create Date: 2021-11-19 17:15:17.017751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1aeb4e245d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deleted_emails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipient', sa.String(length=64), nullable=False),
    sa.Column('subject', sa.String(length=64), nullable=False),
    sa.Column('body', sa.String(length=255), nullable=False),
    sa.Column('filename', sa.String(length=64), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_deleted_emails_subject'), 'deleted_emails', ['subject'], unique=False)
    op.create_table('emails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipient', sa.String(length=64), nullable=False),
    sa.Column('subject', sa.String(length=64), nullable=False),
    sa.Column('body', sa.String(length=255), nullable=False),
    sa.Column('filename', sa.String(length=64), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_emails_subject'), 'emails', ['subject'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('remembers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('remember_hash', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_remembers_user_id'), 'remembers', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_remembers_user_id'), table_name='remembers')
    op.drop_table('remembers')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_emails_subject'), table_name='emails')
    op.drop_table('emails')
    op.drop_index(op.f('ix_deleted_emails_subject'), table_name='deleted_emails')
    op.drop_table('deleted_emails')
    # ### end Alembic commands ###
