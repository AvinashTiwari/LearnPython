require 'rails_helper'

RSpec.describe Article, type: :model do
   it 'should test that factory is valid' do
     expect(FactoryBot.build :article).to be_valid
   end

   it 'should validate the presence of the title' do
     article = FactoryBot.build :article, title: ''
     expect(article).not_to be_valid
     expect(Article.errors.messages[:title]).to include("title can't be blank")
   end

   it 'should validate the presence of the content' do
     article = FactoryBot.build :article, content: ''
     expect(article).not_to be_valid
     expect(Article.errors.messages[:content]).to include("content can't be blank")
   end
end
