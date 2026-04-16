import { describe, it, expect, vi, beforeEach } from 'vitest'
import { mount, flushPromises } from '@vue/test-utils'
import ProductDetail from '../productdetail.vue'
import api from '../../api'

vi.mock('../../api', () => ({
  default: {
    get: vi.fn(),
    post: vi.fn(),
  },
}))

const mockPush = vi.fn()

vi.mock('vue-router', () => ({
  useRoute: () => ({ params: { id: '42' } }),
  useRouter: () => ({ push: mockPush }),
}))

const mockProduct = {
  id: 42,
  name: 'Test Product',
  description: 'A great product',
  price: '12.99',
  stock: 5,
  origin: 'Norway',
  image: 'https://example.com/image.jpg',
}

const mountComponent = () =>
  mount(ProductDetail, {
    global: {
      stubs: { VImg: true, VChip: true },
    },
  })

describe('ProductDetail', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  // ── Rendering ──────────────────────────────────────────────────────────────

  it('renders nothing before product loads', async () => {
    vi.mocked(api.get).mockReturnValue(new Promise(() => {})) // never resolves
    const wrapper = mountComponent()
    expect(wrapper.find('.card').exists()).toBe(false)
  })

  it('renders product name, price, and description after fetch', async () => {
    vi.mocked(api.get).mockResolvedValue({ data: mockProduct })
    const wrapper = mountComponent()
    await flushPromises()

    expect(wrapper.find('h1.title').text()).toBe('Test Product')
    expect(wrapper.find('.price').text()).toContain('$12.99')
    expect(wrapper.find('.description').text()).toBe('A great product')
  })

  // ── Image ──────────────────────────────────────────────────────────────────

  it('renders v-img and hides placeholder when product.image is set', async () => {
    vi.mocked(api.get).mockResolvedValue({ data: mockProduct })
    const wrapper = mountComponent()
    await flushPromises()

    expect(wrapper.findComponent({ name: 'VImg' }).exists()).toBe(true)
    expect(wrapper.find('.empty-image-placeholder').exists()).toBe(false)
  })

  it('shows placeholder and hides v-img when product.image is empty', async () => {
    vi.mocked(api.get).mockResolvedValue({ data: { ...mockProduct, image: '' } })
    const wrapper = mountComponent()
    await flushPromises()

    expect(wrapper.findComponent({ name: 'VImg' }).exists()).toBe(false)
    expect(wrapper.find('.empty-image-placeholder').exists()).toBe(true)
  })

  // ── Button states ──────────────────────────────────────────────────────────

  it('shows "Add to Cart" and enables button when in stock', async () => {
    vi.mocked(api.get).mockResolvedValue({ data: mockProduct })
    const wrapper = mountComponent()
    await flushPromises()

    const button = wrapper.find('button.add-to-cart-button')
    expect(button.text()).toContain('Add to Cart')
    expect(button.attributes('disabled')).toBeUndefined()
  })

  it('shows "Out of stock" and disables button when stock is 0', async () => {
    vi.mocked(api.get).mockResolvedValue({ data: { ...mockProduct, stock: 0 } })
    const wrapper = mountComponent()
    await flushPromises()

    const button = wrapper.find('button.add-to-cart-button')
    expect(button.text()).toContain('Out of stock')
    expect(button.attributes('disabled')).toBeDefined()
  })

  // ── fetchProduct ───────────────────────────────────────────────────────────

  it('calls api.get with the correct product endpoint on mount', async () => {
    vi.mocked(api.get).mockResolvedValue({ data: mockProduct })
    mountComponent()
    await flushPromises()

    expect(api.get).toHaveBeenCalledWith('/products/42/')
  })

  it('redirects to /products when fetch fails', async () => {
    vi.mocked(api.get).mockRejectedValue(new Error('Not found'))
    mountComponent()
    await flushPromises()

    expect(mockPush).toHaveBeenCalledWith('/products')
  })

  // ── addToCart ──────────────────────────────────────────────────────────────

  it('calls api.post with correct payload when Add to Cart is clicked', async () => {
    vi.mocked(api.get).mockResolvedValue({ data: mockProduct })
    vi.mocked(api.post).mockResolvedValue({})
    const wrapper = mountComponent()
    await flushPromises()

    await wrapper.find('button.add-to-cart-button').trigger('click')
    await flushPromises()

    expect(api.post).toHaveBeenCalledWith('/cart/add/', {
      account_id: 1,
      product_id: 42,
      quantity: 1,
    })
  })

  it('shows "Adding..." and disables button while cart request is in flight', async () => {
    vi.mocked(api.get).mockResolvedValue({ data: mockProduct })
    let resolvePost!: () => void
    vi.mocked(api.post).mockReturnValue(new Promise((res) => { resolvePost = () => res({}) }))
    const wrapper = mountComponent()
    await flushPromises()

    wrapper.find('button.add-to-cart-button').trigger('click')
    await wrapper.vm.$nextTick()

    const button = wrapper.find('button.add-to-cart-button')
    expect(button.text()).toContain('Adding...')
    expect(button.attributes('disabled')).toBeDefined()

    resolvePost()
    await flushPromises()

    expect(wrapper.find('button.add-to-cart-button').text()).toContain('Add to Cart')
  })
})
